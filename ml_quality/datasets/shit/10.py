cur.execute("UPDATE public.driver SET name=(%(name)s) WHERE id_driver=(%(id_driver)s)", {"name" : name, "id_driver" : id_driver})
cur.execute("UPDATE public.driver SET surname=(%(surname)s) WHERE id_driver=(%(id_driver)s)", {"surname" : surname, "id_driver" : id_driver})
cur.execute("UPDATE public.driver SET patronymic=(%(patronymic)s) WHERE id_driver=(%(id_driver)s)", {"patronymic" : patronymic, "id_driver" : id_driver})
cur.execute("UPDATE public.driver SET phone_number=(%(phone_number)s) WHERE id_driver=(%(id_driver)s)", {"phone_number" : phone_number, "id_driver" : id_driver})
