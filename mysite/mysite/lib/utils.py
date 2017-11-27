def pagination(request, defaults=(1, 20)):
    """Get pagination parameters from request."""
    p = {}

    try:
        p['per_page'] = int(request.GET.get('per_page'))
        p['page'] = int(request.GET.get('page'))
    except (TypeError, ValueError):
        pass

    sort = request.GET.get('sort', '').split(',')

    if sort[0]:
        p['sort'] = sort
    else:
        p['sort'] = []

    return p
