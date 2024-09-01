from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def visit(request, entry_name):

    entry_content = util.get_entry(entry_name)

    if entry_content is None:
        raise Http404("Page not found!")

    return render(request, "encyclopedia/entry.html", {
        "entryName": entry_name,
        "entry": util.get_entry(entry_name)
    })

def search(request):
    query = request.GET.get('q', '')  # Get the search query from GET request
    if util.get_entry(query) is not None:
        return redirect('visit', entry_name=query)  # Redirect to the entry page if exists
    else:
        return HttpResponse("The requested page was not found.")  # You can handle a search failure differently

def create_new_entry(request):
    return render(request, "encyclopedia/new_entry.html")