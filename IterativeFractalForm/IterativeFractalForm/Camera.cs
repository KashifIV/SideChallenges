using System;
using System.IO;
using System.Drawing;
using System.Windows.Forms;
public class Camera
{
    Point dimensions;
    int posX, posY, posZ;
    int colourSmoothing;
    public Camera(int sizex, int sizey, int smoothing, int x = 0, int y = 0, int z = 0)
    {
        dimensions = new Point(sizex, sizey);
        colourSmoothing = smoothing;
        posX = x;
        posY = y;
        posZ = z;

    }
    public void Draw(PaintEventArgs e)
    {

    }
    public float GetDepthInLength()
    {
        return 0; 
    }
}
