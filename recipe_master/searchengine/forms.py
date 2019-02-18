from haystack.forms import SearchForm

class RecipeSearchForm(SearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()