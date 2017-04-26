
def update_fields(model_inst, request):
    request_dict = request.POST
    for request_key in request_dict.keys():
        if not hasattr(model_inst, request_key):
            continue
        setattr(model_inst, request_key, request_dict.get(request_key))
    model_inst.save()