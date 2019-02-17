import datetime
from haystack import indexes
from master_app.models import Recipe


class RecipeSearch (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    descriptionTags = indexes.CharField(model_attr = 'user', max_length = 20)
 

    def get_model(self):
        return RecipeSearch

    #def index_queryset(self, using=None):
      #  """Used when the entire index for model is updated."""
       # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


