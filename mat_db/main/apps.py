from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class Graph:
    def cyclic_curve(self, data, E):
        K = data.K
        n = data.n
        data=[]
        for sa in range(0, 1000, 10):
            ea=sa/E+(sa/K)**(1/n)
            data.append([ea, sa])
        return data