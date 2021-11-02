print(1194013 % 8)
import shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")

w.poly([[[6,6],[4,4], [6,2],[8,4], [6,6]]])

w.close()