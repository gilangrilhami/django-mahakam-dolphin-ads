class DashboardRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to `dashboard` db.
        """
        if model._meta.app_label == 'dashboard':
            return 'dashboard'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to `dashboard` db.
        """
        if model._meta.app_label == 'dashboard':
            return 'dashboard'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'dashboard' database.
        """
        if app_label == 'dashboard':
            return db == 'dashboard'
        return None