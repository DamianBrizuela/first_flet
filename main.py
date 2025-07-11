import flet as ft

def main(page: ft.Page):
    page.title = "App de flet"

    text = ft.Text("¡Hola, Flet está funcionando!")
    switch = ft.Switch(label="Switch en flet")
    checkbox = ft.Checkbox("¡Esto es un checkbox")
    txtField = ft.TextField(label="Esto es un textfield")
    boton= ft.ElevatedButton("Hacé clic", on_click=lambda e: print("¡Clic!"))

    container = ft.Container(
        content= ft.Column([
            text,
            checkbox,
            switch
        ]),
        padding= 10,
        bgcolor= "lightgray"
    )

    row = ft.Row([
        txtField,
        boton
    ])

    page.add(container, row)

    page.add(
        ft.Column([
            ft.Text("Vertical (Column)", size=20),
            ft.Column([
                ft.Text("Uno"),
                ft.Text("Dos"),
                ft.Text("Tres")
            ], spacing=5),

            ft.Text("Horizontal (Row)", size=20),
            ft.Row([
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C")
            ], alignment="spaceEvenly", expand=True)
        ])
    )    

ft.app(target=main)
