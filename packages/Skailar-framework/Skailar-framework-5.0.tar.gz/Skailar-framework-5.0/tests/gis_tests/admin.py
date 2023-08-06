try:
    from skailar.contrib.gis import admin
except ImportError:
    from skailar.contrib import admin

    admin.GISModelAdmin = admin.ModelAdmin
