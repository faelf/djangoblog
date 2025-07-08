from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
class PostList(generic.ListView):
  queryset = Post.objects.all()
  template_name = "blog/index.html"
  paginate_by = 3

def post_detail(request, slug):
  """
  Display an individual :model:`blog.Post`.

  **Context**

  ``post``
      An instance of :model:`blog.Post`.

  **Template:**

  :template:`blog/post_detail.html`
  """

  queryset = Post.objects
  post = get_object_or_404(queryset, slug=slug)

  return render(
      request,
      "blog/post_detail.html",
      {"post": post},
  )