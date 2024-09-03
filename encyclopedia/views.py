import random
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from .forms import MarkdownForm
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def visit(request, entry_name):

    entry_content = util.get_entry(entry_name)

    if entry_content is None:
        raise Http404("Page not found!")
    
    entry_html = markdown.markdown(entry_content)

    return render(request, "encyclopedia/entry.html", {
        "entryName": entry_name,
        "entry": entry_html
    })

def search(request):
    query = request.GET.get('q', '')  # Get the search query from GET request
    if util.get_entry(query) is not None:
        return redirect('visit', entry_name=query)  # Redirect to the entry page if exists
    else:
        return HttpResponse("The requested page was not found.")  # You can handle a search failure differently
    
def entry(request):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)
        title = request.POST.get('title')
        entries = util.list_entries()
        if form.is_valid() and title not in entries:
            markdown_content = form.cleaned_data['content']
            util.save_entry(title, markdown_content)
            return redirect('index')
        else:
            return HttpResponse("Title already exists!")
    else:
        form = MarkdownForm()

    return render(request, "encyclopedia/markdown_form.html", {'form': form})

def edit_entry(request, entry_name):
    if request.method == 'POST':
        form = MarkdownForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(entry_name, content)
            return redirect('visit', entry_name=entry_name)
    else:
        entry_content = util.get_entry(entry_name)
        if entry_content is None:
            raise Http404("Page not found")
        form = MarkdownForm(initial={'title': entry_name, 'content': entry_content})

    return render(request, "encyclopedia/edit_entry.html", {
        "form": form,
        "entryName": entry_name
    })

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('visit', entry_name = random_entry)
    else:
        raise Http404("No entries available!")