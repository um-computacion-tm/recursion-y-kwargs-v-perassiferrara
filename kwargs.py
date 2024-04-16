def buscar_datos(*args, **kwargs):

    correcto = 0
    for persona in kwargs.keys():
        for dato in args:
            if dato in kwargs[persona].values():
                correcto += 1
        if correcto == len(args):
            return {persona : kwargs[persona]}


database = {
            "persona1":{
                    "primer_nombre":"Pablo",
                    "segundo_nombre":"Diego",
                    "primer_apellido":"Ruiz",
                    "segundo_apellido":"Picasso"
                    }
            ,
            "persona2":{
                    "primer_nombre":"Jorge",
                    "segundo_nombre":"Roman",
                    "primer_apellido":"Castro",
                    "segundo_apellido":"Sanchez"
                    }
            ,
            "persona3":{
                    "primer_nombre":"Osvaldo",
                    "primer_apellido":"Cerro",
                    }
            ,
            "persona4":{
                    "primer_nombre":"Luis",
                    "segundo_nombre":"Damian",
                    "tercer_nombre":"Rodolfo",
                    "primer_apellido":"Lucero",
                    "segundo_apellido":"Perez"
                    }
            }