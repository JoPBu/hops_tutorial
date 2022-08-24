from flask import Flask
import ghhops_server as hs
import rhino3dm
import os

# Hops als Middleware registrieren
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

dir_path = os.path.dirname(os.path.realpath(__file__))


# Definition von Component 1
@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    icon = os.path.join(dir_path, "recources\\icon_add.png"),
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        #hs.HopsNumber("B", "B", "Second number"),
        hs.HopsNumber("B", "B", "Second number", hs.HopsParamAccess.LIST),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)

# Programm 1
def add(a: float, b: float):
    list = []
    for i in b:
        list.append(a+i)
    return list

# Component 2
@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
# Funktion 2
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

# Starten des Flask servers
if __name__ == "__main__":
    app.run(host='localhost', port=6000,debug=True)