import elements as e

class ChangeScene:
    def __init__(self):
        self.set_img = None
        self.rect_img = None

    def make_image(self,img):

        self.set_img = e.Fit_rect_size.fit_to_rect(img)
        self.rect_img = self.set_img.get_rect()
        
    def blit(self,screen):
        screen.blit(self.set_img,self.rect_img)