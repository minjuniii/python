import turtle as t
 
n = 100
t.shape('turtle')
for i in range(n):
    t.begin_fill()
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)
