from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView


from movies.models import FilmWork

PAGINATE_MOVIES_PER_PAGE = 50

class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']


    def get_queryset(self):
        qs = FilmWork.objects.values('id', 'title', 'description', 'creation_date', 'rating', 'type').annotate(
            genres=ArrayAgg('genres__name', distinct=True),
            actors=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='actor'), distinct=True),
            directors=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='director'), distinct=True),
            writers=ArrayAgg('persons__full_name', filter=Q(personfilmwork__role='writer'), distinct=True)
            )

        return qs

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    # model = FilmWork
    http_method_names = ['get']
    paginate_by = PAGINATE_MOVIES_PER_PAGE

    def get_context_data(self):
        queryset = self.get_queryset()

        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset, self.paginate_by)

        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    # model = FilmWork

    def get_context_data(self, **kwargs) -> JsonResponse:
        return {**kwargs["object"]}