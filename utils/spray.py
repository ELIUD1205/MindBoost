class Spray():
    def __init__(self, base_image, hover_image, pos):
        # Imágenes para el estado normal y "hover"
        self.base_image = base_image
        self.hover_image = hover_image
        self.image = self.base_image  # Imagen que se muestra por defecto
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeImage(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.hover_image  # Cambia a la imagen de "hover"
        else:
            self.image = self.base_image  # Vuelve a la imagen base