using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace IterativeFractalForm
{
    public partial class Form1 : Form
    {
        const int SIZEX = 1280;
        const int SIZEY = 720;
         int ITERATIONS = 100;
         float MINREAL = -2.13f;
         float MAXREAL = 1.33f;
         float MINIMAGINARY = -1.0f;
         float MAXIMAGINARY = 1.0f;
        bool zoom = false;
        bool left, right, up, down; 
        public Form1()
        {
            InitializeComponent();
            Refresh(); 
        }
        float GetY(int y)
        {
            return y * ((MAXIMAGINARY - MINIMAGINARY) / SIZEY) + MINIMAGINARY;
        }
        float GetX(int x)
        {
            return x * ((MAXREAL - MINREAL) / SIZEX) + MINREAL; 
        }
        int Calculation(float x, float y)
        {
            float zx = 0f;
            float zy = 0f; 
            int maxiter = ITERATIONS;
            int i = 0;
            int value = -1; 
            while ((zx * zx) + (zy * zy) < 4.0 && i < maxiter)
            {
                float temp = (zx * zx) - (zy * zy) + x;
                zy = 2 * zx * zy + y;
                zx = temp; 
                i++; 
            }

            if (i == ITERATIONS)
                value = -1;
            else
                value = i; 
            return value; 
        }
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            for (int y = 0; y < SIZEY; y++) 
                for (int x = 0; x < SIZEX; x++)
                {
                    int value = Calculation(GetX(x), GetY(y));
                    Brush col;
                    if (value == -1)
                        col = (Brush)Brushes.Black;
                    else
                    {
                        int temp = (int)(value/(float)ITERATIONS*255f*3f);
                        int b = 255;
                        temp -= b;
                        if (temp < 0)
                            b -= Math.Abs(temp);
                        int g = 255;
                        temp -= g;
                        if (temp < 0)
                            g -= Math.Abs(temp);
                        int r = 255;
                        temp -= r;
                        if (temp < 0)
                            r -= Math.Abs(temp);

                        var colour = new SolidBrush(Color.FromArgb(255, (byte)r, (byte)g, (byte)b));
                        col = colour; 
                    }
                    e.Graphics.FillRectangle(col, x, y, 1, 1); 
                }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (zoom)
            {
                float power = MAXIMAGINARY - MINIMAGINARY;
                power /= 8;
                MAXIMAGINARY -= power;
                MINIMAGINARY += power;
                power = MAXREAL - MINREAL;
                power /= 8; 
                MINREAL += power;
                MAXREAL -= power;
                Refresh(); 
            }
            else
            {
                float powerY = MAXIMAGINARY - MINIMAGINARY;
                powerY /= 8;
                float powerX = MAXREAL -MINREAL;
                powerX /= 8;

                if (right)
                {
                    MINREAL += powerX;
                    MAXREAL += powerX;
                    Refresh();
                }
                else if (left)
                {
                    MINREAL -= powerX;
                    MAXREAL -= powerX;
                    Refresh();
                }
                else if (up)
                {
                    MAXIMAGINARY += powerY;
                    MINIMAGINARY += powerY;
                    Refresh();
                }
                else if (down)
                {
                    MAXIMAGINARY -= powerY;
                    MINIMAGINARY -= powerY;
                    Refresh(); 
                }
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.W)
            {
                zoom = true;
                ITERATIONS += 15; 
            }
            else if (e.KeyCode == Keys.A)
                left = true;
            else if (e.KeyCode == Keys.D)
                right = true;
            else if (e.KeyCode == Keys.S)
                down = true; 
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.W)
                zoom = false;
            if (e.KeyCode == Keys.A)
                left = false;
            if (e.KeyCode == Keys.D)
                right = false;
            if (e.KeyCode == Keys.S)
                down = false;
        }
    }
}
