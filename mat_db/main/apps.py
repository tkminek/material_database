from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class Graph:
    @staticmethod
    def cyclic_curve(data, e):
        k = data.K
        n = data.n
        data = []
        for sa in range(0, 1000, 10):
            ea = sa/e+(sa/k)**(1/n)
            if ea >= 0.5:
                break
            else:
                data.append([ea, sa])
        return data

    @staticmethod
    def en_curve(data, e):
        sf = data.Sf
        b = data.b
        c = data.c
        ef = data.Ef
        data = []
        nf = 1
        while nf < int(5e11):
            ea = sf/e*(nf**b)+ef*(nf**c)
            data.append([nf, ea])
            nf *= 10
        return data

    @staticmethod
    def sn_curve(data):
        sa = data.Sa.split(",")
        nf = data.Nf.split(",")
        data = []
        for s, c in zip(sa, nf):
            data.append([float(c), round(float(s), 1)])
        return data

    @staticmethod
    def static_curve(data, e):
        k = data.K
        n = data.n
        data = []
        for sa in range(0, 1000, 10):
            ea = sa / e + (sa / k) ** (1 / n)
            if ea >= 0.5:
                break
            data.append([ea, sa])
        return data

    @staticmethod
    def custom_curve(data):
        x_value = data.x_value.split(",")
        y_value = data.y_value.split(",")
        data_axis_type = {"x_axis_type": data.x_axis_type, "y_axis_type": data.y_axis_type}
        data_axis = {"x_axis": data.x_axis, "y_axis": data.y_axis}
        data_value = []
        for xv, yv in zip(x_value, y_value):
            data_value.append([float(xv), float(yv)])
        return data_axis, data_value, data_axis_type
