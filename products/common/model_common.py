def default_meta(model):
    class Meta:
        abstract = False
        ordering = ['-created_at']
    model.Meta = Meta
    return model
