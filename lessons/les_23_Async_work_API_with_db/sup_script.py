# from models.db_sync import main
#
# main()


from views.users_sync.views import get_user_by_id

for i in range(200):
    print(f"{i:03d}")
