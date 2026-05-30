import pygame
import random
import math

# تنظیمات اولیه
pygame.init()

# ابعاد صفحه
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clash of Saied")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# بارگذاری تصاویر
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (100, 100))

enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (100, 100))

bullet_image = pygame.image.load("bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (10, 5))

# تصویر گلوله‌های دشمن
enemy_bullet_image = pygame.image.load("enemy_bullet.png")
enemy_bullet_image = pygame.transform.scale(enemy_bullet_image, (10, 5))

# تصویر قلب قرمز برای خون
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (30, 30))

# تصویر چمن زیر پلتفرم‌ها
grass_image = pygame.image.load("grass.png")
grass_image = pygame.transform.scale(grass_image, (WIDTH, 100))  # چمن به اندازه صفحه

# کاراکتر اصلی
player_width = 100
player_height = 50
player_x = 100
player_y = HEIGHT - player_height - 100
player_velocity = 10
player_jump = False
player_jump_height = 10
player_vel_y = 0
player_health = 10  # خون بازیکن

# زمین
ground_y = HEIGHT - 100
ground_height = 40

# دشمن‌ها
enemy_width = 100
enemy_height = 50
enemy_velocity = 3
enemies = []

# گلوله‌های بازیکن
player_bullets = []

# گلوله‌های دشمن
enemy_bullets = []

# تنظیمات بازی
clock = pygame.time.Clock()
run_game = True
kills = 0  # تعداد کشته‌های دشمن

# تابع برای نمایش کاراکتر
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# تابع برای نمایش دشمن‌ها
def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

# تابع برای نمایش گلوله‌ها
def draw_bullets(bullets, image):
    for bullet in bullets:
        screen.blit(image, bullet)

# تابع برای حرکت گلوله‌ها
def move_bullets(bullets, velocity):
    global player_bullets, enemy_bullets
    for bullet in bullets:
        bullet.x += velocity
        if bullet.x < 0 or bullet.x > WIDTH:
            bullets.remove(bullet)

# تابع برای ایجاد دشمن جدید
def create_enemy():
    enemy_x = random.randint(WIDTH, WIDTH + 500)
    enemy_y = ground_y - enemy_height
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))

# تابع برای حرکت دشمن‌ها به سمت بازیکن
def move_enemies():
    global enemies
    for enemy in enemies:
        # محاسبه جهت حرکت به سمت بازیکن (فقط جهت افقی)
        direction_x = player_x - enemy.x
        direction_y = 0  # جهت عمودی را صفر می‌کنیم تا دشمن به بالا یا پایین نرود

        # محاسبه فاصله بین دشمن و بازیکن (فقط جهت افقی)
        distance = abs(direction_x)  # فقط فاصله افقی محاسبه می‌شود

        # نرمال‌سازی جهت حرکت (فقط جهت افقی)
        if distance != 0:
            direction_x /= distance

        # حرکت دشمن به سمت بازیکن (فقط جهت افقی)
        enemy.x += direction_x * enemy_velocity

        # حذف دشمن اگر از صفحه خارج شود
        if enemy.x < -enemy_width:
            enemies.remove(enemy)

# تابع برای شلیک گلوله‌های دشمن
def enemy_shoot(direction='down'):
    for enemy in enemies:
        if random.randint(1, 100) == 1:  # شلیک تصادفی دشمن
            # محاسبه موقعیت x گلوله (وسط دشمن)
            bullet_x = enemy.x + enemy_width // 2 - 5  # 5 نصف عرض گلوله است
            # محاسبه موقعیت y گلوله بر اساس جهت
            if direction == 'down':
                bullet_y = enemy.y + 13  # پایین دشمن
            elif direction == 'up':
                bullet_y = enemy.y  # بالای دشمن
            else:
                raise ValueError("جهت نامعتبر! از 'up' یا 'down' استفاده کنید.")

            # ایجاد یک شیء Rect برای گلوله
            bullet = pygame.Rect(bullet_x, bullet_y, 10, 5)  # (x, y, width, height)
            # اضافه کردن گلوله به لیست گلوله‌های دشمن
            enemy_bullets.append(bullet)

# تابع برای برخورد گلوله‌ها با دشمن
def check_collisions():
    global player_bullets, enemy_bullets, enemies, player_health, kills
    for bullet in player_bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                player_bullets.remove(bullet)
                kills += 1
                break
    for enemy in enemies:
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(enemy):
            player_health -= 1  # کاهش خون بازیکن
            enemies.remove(enemy)
            if player_health <= 0:
                print("شما کشته شدید!")
                pygame.quit()
                exit()
    for bullet in enemy_bullets:
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(bullet):
            player_health -= 1
            enemy_bullets.remove(bullet)
            if player_health <= 0:
                print("شما کشته شدید!")
                pygame.quit()
                exit()

# تابع برای شلیک گلوله‌های بازیکن
def player_shoot(direction='down'):
    # محاسبه موقعیت x گلوله (وسط بازیکن)
    bullet_x = player_x + player_width // 2 - -16  # 5 نصف عرض گلوله است
    # محاسبه موقعیت y گلوله بر اساس جهت
    if direction == 'up':
        bullet_y = player_y  # بالای بازیکن
    elif direction == 'down':
        bullet_y = player_y + 13  # پایین بازیکن
    else:
        raise ValueError("جهت نامعتبر! از 'up' یا 'down' استفاده کنید.")

    # ایجاد یک شیء Rect برای گلوله
    bullet = pygame.Rect(bullet_x, bullet_y, 10, 5)  # (x, y, width, height)
    # اضافه کردن گلوله به لیست گلوله‌های بازیکن
    player_bullets.append(bullet)


# حلقه بازی
while run_game:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    keys = pygame.key.get_pressed()

    # حرکت چپ و راست کاراکتر
    if keys[pygame.K_LEFT]:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT]:
        player_x += player_velocity

    # پرش کاراکتر
    if keys[pygame.K_UP] and not player_jump:
        player_jump = True
        player_vel_y = -15  # سرعت پرش

    # فیزیک پرش
    if player_jump:
        player_y += player_vel_y
        player_vel_y += 0.60  # گرانش
        if player_y >= ground_y - player_height:
            player_y = ground_y - player_height
            player_jump = False
            player_vel_y = 0

    # اضافه کردن دشمن جدید
    if random.randint(1, 50) == 1:  # ایجاد دشمن با احتمال کم
        create_enemy()

    # شلیک گلوله‌های بازیکن
    if keys[pygame.K_SPACE]:
        player_shoot()

    # حرکت دشمن‌ها
    move_enemies()

    # حرکت گلوله‌های بازیکن
    move_bullets(player_bullets, 20)

    # حرکت گلوله‌های دشمن
    move_bullets(enemy_bullets, -5)

    # شلیک گلوله‌های دشمن
    enemy_shoot()

    # بررسی برخورد گلوله‌ها با دشمن
    check_collisions()

    # نمایش چمن
    screen.blit(grass_image, (0, HEIGHT - 70))  # نمایش چمن در پایین صفحه

    # نمایش کاراکتر
    draw_player(player_x, player_y)

    # نمایش دشمن‌ها
    draw_enemies()

    # نمایش گلوله‌های بازیکن
    draw_bullets(player_bullets, bullet_image)

    # نمایش گلوله‌های دشمن
    draw_bullets(enemy_bullets, enemy_bullet_image)

    # نمایش تعداد جان‌های بازیکن در دو خط
    max_hearts_per_line = 5  # حداکثر تعداد قلب‌ها در هر خط
    heart_spacing = 35  # فاصله بین قلب‌ها
    start_x = 10  # موقعیت شروع افقی
    start_y = 10  # موقعیت شروع عمودی

    for i in range(player_health):
        # محاسبه موقعیت x و y برای هر قلب
        if i < max_hearts_per_line:
            # خط اول
            heart_x = start_x + i * heart_spacing
            heart_y = start_y
        else:
            # خط دوم
            heart_x = start_x + (i - max_hearts_per_line) * heart_spacing
            heart_y = start_y + heart_spacing  # فاصله عمودی برای خط دوم

        # نمایش قلب روی صفحه
        screen.blit(heart_image, (heart_x, heart_y))

    # نمایش تعداد کشته‌های دشمن
    font = pygame.font.SysFont("Arial", 30)
    kills_text = font.render(f"Kills: {kills}", True, BLACK)
    screen.blit(kills_text, (WIDTH - 150, 10))

    # بروزرسانی صفحه
    pygame.display.update()

    # کنترل سرعت بازی
    clock.tick(55)

pygame.quit()
