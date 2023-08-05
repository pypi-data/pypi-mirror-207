import torch
import torch.fft
import torch.nn as nn


class FeedForward(nn.Module):
    def __init__(self, dim, mult = 4, dropout = 0.):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(dim, dim * mult, 1),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Conv2d(dim * mult, dim, 1),
            nn.Dropout(dropout)
        )
    def forward(self, x):
        return self.net(x)

class FourierBlock(nn.Module):
    def __init__(
        self,
        *,
        final_dim = 16,
        dropout = 0.,
        mlp_mult = 1
    ):
        super().__init__()
        
        self.ff = nn.Sequential(
            nn.BatchNorm2d(final_dim),
            FeedForward(final_dim, mlp_mult, dropout = dropout)
        )

        
    def forward(self, x):

        x = torch.fft.fft(torch.fft.fft2(x), dim=1).real
        
        x = self.ff(x)
        
        return x
        
class FNet2D(nn.Module):
    def __init__(
        self,
        *,
        num_classes,
        depth,
        final_dim = 16,
        dropout = 0.,
        mlp_mult = 1, 
    ):
        super().__init__()
        
        self.layers = nn.ModuleList([])
        for _ in range(depth):
            self.layers.append(FourierBlock(final_dim = final_dim, dropout = dropout, mlp_mult = mlp_mult))
        
        self.pool = nn.Sequential(
            nn.AdaptiveAvgPool2d((1,1)),
            nn.Flatten(),
            nn.Linear(final_dim, num_classes)
        )

        self.conv = nn.Sequential(
            nn.Conv2d(3, int(final_dim/2), 3, 1, 1),
            nn.Conv2d(int(final_dim/2), final_dim, 3, 1, 1)
        )

      

    def forward(self, img):
        x = self.conv(img)  
 
        for attn in self.layers:
            x = attn(x) + x

        out = self.pool(x)

        return out
      
