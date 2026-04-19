def is_teacher_or_admin(user):
    return user.is_authenticated and user.role in ['teacher', 'admin']