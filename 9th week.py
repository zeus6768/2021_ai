# pytorch
import torch

## 편미분
a = torch.tensor(3, dtype=torch.float, requires_grad=True)
b = torch.tensor(4, dtype=torch.float, requires_grad=True)
c = a * b
c.backward()
print(a.grad)
print(b.grad)

## 
a = torch.ones(3, requires_grad=True)
b = a + 1
c = b * b
print(a.grad)
print(a.grad_fn)
print(b.grad)

d = c.sum()
d.backward