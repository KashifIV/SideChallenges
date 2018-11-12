using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing; 
using System.Windows.Forms;

namespace RecmanSum
{
    public partial class RecmanVisualization : Form
    {
        const int SIZEX = 1280;
        const int SIZEY = 720;
        const int n = 100;
        int max = 0;
        Label lblCount; 
        List<int> sequence;
        int animationCount = 0; 
        public RecmanVisualization()
        {
            InitializeComponent();
            InitializeSequence(n);
            InitializeCount(); 
        }
        void InitializeSequence(int n)
        {
            sequence = new List<int>(n);             
            HashSet<int> set = new HashSet<int>(sequence); 
            int count = 0;
            set.Add(count);
            sequence.Add(count);
            int current = 0; 
            for (int i = 1; i < n; i++)
            {
                if (current -i > 0 && !set.Contains(current - i))
                {
                    current -= i; 
                    sequence.Add(current);
                    set.Add(current);
                }
                else
                {
                    current += i;
                    sequence.Add(current);
                    set.Add(current); 
                }
                if (current > max)
                    max = current; 
            }          
        }
        void DrawNumberLine(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(new Pen((Brush)Brushes.Black), new Rectangle(new Point(0, SIZEY / 2), new Size(SIZEX, 2))); 
        }
        Point FindPoint(int a)
        {
            int cut = SIZEX / max;
            return new Point(cut * a, SIZEY / 2); 
        }
        void InitializeCount()
        {
            lblCount = new Label();
            lblCount.Enabled = true;
            lblCount.Text = animationCount.ToString();
            lblCount.BackColor = Color.White;
            lblCount.BringToFront(); 
            this.Controls.Add(lblCount); 
        }
        void UpdateCount()
        {
            lblCount.Text = animationCount.ToString(); 
        }
        void DrawTo(int a, int b, bool upper, int sub, PaintEventArgs e)
        {
            Point pos_a = FindPoint(a);
            Point pos_b = FindPoint(b);
            int len;
            Rectangle bound; 
            if (b > a)
            {
                len = pos_b.X - pos_a.X;
                bound = new Rectangle(new Point(pos_a.X, pos_a.Y - len / 2), new Size(len, len));
            }
            else
            {
                len = pos_a.X - pos_b.X;
                bound = new Rectangle(new Point(pos_b.X, pos_b.Y - len / 2), new Size(len, len));
            }

            if (animationCount - (sub * 180) > 0)
            {
                float deg = Math.Abs(animationCount - sub * 180);
                if (deg > 180)
                    deg = 180;
                if (upper)
                {
                    if (a < b)
                        e.Graphics.DrawArc(new Pen(Color.FromArgb(255, Math.Abs(255 - sub), 13 + sub, Math.Abs(255 - sub)), 1.8f), bound, 180, deg);
                    else
                        e.Graphics.DrawArc(new Pen(Color.FromArgb(255, Math.Abs(255 - sub), 13 + sub, Math.Abs(255 - sub)), 1.8f), bound, 0, -deg);
                }
                else
                {
                    if (a < b)
                        e.Graphics.DrawArc(new Pen(Color.FromArgb(255, Math.Abs(232 - sub), 12 + sub, Math.Abs(122 - sub)), 1.8f), bound, 180, -deg);
                    else
                        e.Graphics.DrawArc(new Pen(Color.FromArgb(255, Math.Abs(232 - sub), 12 + sub, Math.Abs(122 - sub)), 1.8f), bound, 0, deg);
                }
            
            }
                    
        }
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            DrawNumberLine(e);
            bool upper = true; 
            for (int i = 0; i < n-1; i++)
            {
                DrawTo(sequence[i], sequence[i + 1], upper, i, e);
            
                upper = !upper; 
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            animationCount+=4;
            UpdateCount(); 
            Refresh(); 
        }
    }
}
