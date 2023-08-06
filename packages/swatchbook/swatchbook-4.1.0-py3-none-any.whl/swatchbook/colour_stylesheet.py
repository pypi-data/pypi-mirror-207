
from graphlib import TopologicalSorter, CycleError

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.http import Http404


def update_colour_stylesheet_file(file_name='colours.css', prefix=''):

    text = build_stylesheet_definitions(prefix=prefix)
    file = ContentFile(text)
    save_file("swatchbook/" + file_name, file)


def build_stylesheet_definitions(colours=None, prefix=''):

    formatted_prefix = prefix

    if formatted_prefix:
        formatted_prefix = formatted_prefix + '-'

    from .models import Colour, MediaQuery

    if colours is None:
        colours = Colour.objects.all()

    colours = colours.order_by('identifier')

    queries = MediaQuery.objects.all().filter(active=True).order_by('-priority', 'identifier')

    query_scopes = {}

    nodes = {}

    for colour in colours:
        css_identifier = "--{}{}".format(formatted_prefix, colour.identifier)

        default_colour = colour.definition['default']
        css_colour = default_colour.block.define_css_expression(default_colour, prefix)
        css_declaration = "  {}: {};".format(css_identifier, css_colour)

        variable = default_colour.block.extract_css_variable(default_colour, prefix)

        if variable:
            deps = (variable,)
        else:
            deps = ()

        node = css_identifier, css_declaration, deps
        nodes[css_identifier] = node

        conditionals = colour.definition['conditionals']

        for conditional_definition in conditionals:
            conditional_colour = conditional_definition.value['colour']
            css_conditional_colour = conditional_colour.block.define_css_expression(conditional_colour, prefix)

            if not css_conditional_colour:
                continue

            css_declaration = "    {}: {};".format(css_identifier, css_conditional_colour)

            variable = conditional_colour.block.extract_css_variable(conditional_colour, prefix)

            if variable:
                deps = (variable,)
            else:
                deps = ()

            query = conditional_definition.value['query']

            if not query:
                continue

            if query.id not in query_scopes:
                query_scopes[query.id] = {}

            node = css_identifier, css_declaration, deps
            query_scopes[query.id][css_identifier] = node

    """
    from .models import ColourAlias

    aliases = ColourAlias.objects.all()

    for alias in aliases:
        target = alias.colour

        if target is None:
            continue

        css_identifier = "--{}".format(alias.alias)
        css_declaration = "    {}: var(--{});".format(css_identifier, target.identifier)

        deps = {"--{}".format(target.identifier)}
        node = css_identifier, css_declaration, deps
        nodes[css_identifier] = node
    """

    graph = {node: {nodes[dep] for dep in node[2] if dep in nodes} for node in nodes.values()}

    try:
        css_declarations = [node[1] for node in TopologicalSorter(graph).static_order()]
    except CycleError:
        css_declarations = []

    css_declarations = "\n".join(css_declarations)
    css_declarations = ":root {{\n{}\n}}\n".format(css_declarations)

    for query in queries:

        if query.id not in query_scopes:
            continue

        nodes = query_scopes[query.id]
        graph = {node: {nodes[dep] for dep in node[2] if dep in nodes} for node in nodes.values()}

        try:
            scope_css_declarations = [node[1] for node in TopologicalSorter(graph).static_order()]
        except CycleError:
            scope_css_declarations = []

        scope_css_declarations = "\n".join(scope_css_declarations)

        css_media_query = "@media " + query.definition + " {\n  :root {\n"
        css_declarations += "\n\n" + css_media_query + scope_css_declarations + "\n  }\n}\n"

    result = '@charset "UTF-8";\n\n{}\n'.format(css_declarations)
    return result


def save_file(local_path, content):

    available_path = default_storage.get_available_name(local_path)

    if local_path != available_path:
        default_storage.delete(local_path)

    try:
        local_path = default_storage.path(local_path)
    except NotImplementedError:
        local_path = None

    if local_path is None:
        raise Http404

    file = default_storage.save(local_path, content)
    return file


def open_file(local_path, mode="rb"):

    try:
        local_path = default_storage.path(local_path)
    except NotImplementedError:
        local_path = None

    if local_path is None:
        raise Http404

    file = default_storage.open(local_path, mode=mode)
    return file


# noinspection PyMethodMayBeStatic
def load_file_text(file):

    charset = None

    if hasattr(file, 'charset'):
        charset = file.charset

    if charset is None:
        charset = "utf-8"

    file.seek(0)
    file_bytes = file.read()
    file_text = file_bytes.decode(encoding=charset)
    return file_text
