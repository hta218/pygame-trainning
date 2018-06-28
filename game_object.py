game_objects = []


def add(obj):
    game_objects.append(obj)


def update():
    for obj in game_objects:
        obj.update()


def render(canvas):
    for obj in game_objects:
        # if obj.image is not None:
        #     canvas.blit(obj.image, (obj.x, obj.y))
        if obj.is_active:
            obj.render(canvas)

def collide_with(box_collider, obj_type):
    for obj in game_objects:
        if type(obj) == obj_type and obj.is_active:
            if obj.box_collider.collide_with(box_collider):
                return obj

    return None

def recycle(obj_type, x, y):
    for obj in game_objects:
        if obj_type == type(obj) and not obj.is_active:
            obj.is_active = True
            obj.x = x
            obj.y = y
            return obj

    new_obj = obj_type(x, y)
    add(new_obj)
    return new_obj


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.box_collider = None
        self.is_active = True

    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        print(len(game_objects))
        if self.image is not None:
            w = self.image.get_width()
            h = self.image.get_height()

            render_pos = (self.x - w / 2, self.y - h / 2)

            canvas.blit(self.image, render_pos)

        if self.box_collider is not None:
            self.box_collider.render(canvas)

    def deactivate(self):
        self.is_active = False