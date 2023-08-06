
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.http import Http404

from .blocks import define_css_color


def update_variable_stylesheet_file():

    text = build_stylesheet_definitions()
    file = ContentFile(text)
    save_file("swatchbook/variables.css", file)


def build_stylesheet_definitions(variables=None):

    from .models import StylesheetVariable, MediaQuery

    if variables is None:
        variables = StylesheetVariable.objects.all()

    variables = variables.order_by('identifier')

    queries = MediaQuery.objects.all().filter(active=True).order_by('-priority', 'identifier')

    query_scopes = {}

    css_declarations = []

    for variable in variables:
        css_identifier = "--{}".format(variable.identifier)
        css_declaration = "  {}: {};".format(css_identifier, variable.definition)
        css_declarations.append(css_declaration)

        for conditional_definition in variable.conditional_definitions:

            definition = conditional_definition.value['definition']

            css_declaration = "    {}: {};".format(css_identifier, definition)

            query = conditional_definition.value['query']

            if not query:
                continue

            if query.id not in query_scopes:
                query_scopes[query.id] = []

            query_scopes[query.id].append(css_declaration)

    css_declarations = "\n".join(css_declarations)
    css_declarations = ":root {{\n{}\n}}\n".format(css_declarations)

    for query in queries:

        if query.id not in query_scopes:
            continue

        scope_css_declarations = "\n".join(query_scopes[query.id])
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
