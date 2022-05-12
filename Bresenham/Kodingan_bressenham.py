# Nama          : Tatsbita Thifalia
# Nim           : 20051397027
# Prodi/Kelas   : D4 Manajemen Informatika/2020 A


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    # layar dan memberikan warna
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(128.0,0.0, 0.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # grid dan ukurannya 640 x 480
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgBresenham(inputx0, inputx1, inputy0, inputy1):
    # titik awal dan akhir
    x0 = inputx0
    y0 = inputy0
    x1 = inputx1
    y1 = inputy1
    x = x0
    y = y0

    # dx dan dy
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # hitung p (parameter) 
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    # tentukan titik awal dan akhir
    if (x0 > x1):
        x = x1
        y = y1
        xend = x0
    else:
        x = x0
        y = y0
        xend = x1
    

    # gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)

    # perulangan untuk menggambar 
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y0 > y1):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':

    x0 = 250
    y0 = 300
    x1 = 400
    y1 = 30

    glutInit()
    # inisialisasi ukuran layar glut
    glutInitWindowSize(640,480)

    # inisialisasi title window
    glutCreateWindow("Bresenham")

    # inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    # inisialisasi pembuatan window
    glutDisplayFunc(lambda: AlgBresenham(x0, x1, y0, y1))
    glutIdleFunc(lambda: AlgBresenham(x0, x1, y0, y1))

    # memanggil fungsi setingan layar setelah fungsi algoritma dijalankan
    initFun()
    glutMainLoop()