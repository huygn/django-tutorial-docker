"""
Configurations for local development.
"""

def show_toolbar(request):
    """
    For showing django-debug-toolbar when running inside docker.
    credit: https://gist.github.com/douglasmiranda/9de51aaba14543851ca3
    """
    if request.is_ajax():
        return False
    return True
