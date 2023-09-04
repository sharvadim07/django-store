from typing import Optional


class CommonMixin:
    title: Optional[str] = None

    def get_context_data(self, **kwargs):
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context["title"] = self.title
        return context
