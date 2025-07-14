from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.contrib import messages

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
  comments = post.comments.all().order_by("-created_on")
  comment_count = post.comments.filter(approved=True).count()
  if request.method == "POST":
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

  comment_form = CommentForm()

  return render(
      request,
      "blog/post_detail.html",
      {
          "post": post,
          "comments": comments,
          "comment_count": comment_count,
          "comment_form": comment_form,
      },
  )