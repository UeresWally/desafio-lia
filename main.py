courses = {
    "espanhol": {
      "iniciante": {
        "manha": [
          {
            "id": 1
          },
          {
            "id": 2
          }
        ],
        "noite": [
          {
            "id": 3
          },
          {
            "id": 4
          }
        ]
      },
      "avancado": {
        "manha": [
          {
            "id": 5
          },
          {
            "id": 6
          }
        ]
      }
    },
    "ingles": {
      "avancado": {
        "manha": [
          {
            "id": 11
          },
          {
            "id": 21
          }
        ]
      }
    }
  }
def search(courses, params=None):
    result = []
    
    def extract_ids(data):
        return [{"id": item["id"]} for item in data]
    
    if params is None:
        for idioma_data in courses.values():
            for niveis_data in idioma_data.values():
                for periodos_data in niveis_data.values():
                    result.extend(extract_ids(periodos_data))
    else:
        idioma_param = params[0] if len(params) > 0 else None
        nivel_param = params[1] if len(params) > 1 else None
        periodo_param = params[2] if len(params) > 2 else None
        
        for idioma, idioma_data in courses.items():
            if idioma_param is None or idioma_param == idioma:
                if nivel_param is None:
                    for nivel_data in idioma_data.values():
                        if periodo_param is None:
                            for periodos_data in nivel_data.values():
                                result.extend(extract_ids(periodos_data))
                        else:
                            if periodo_param in nivel_data:
                                result.extend(extract_ids(nivel_data[periodo_param]))
                elif nivel_param in idioma_data:
                    if periodo_param is None:
                        for periodos_data in idioma_data[nivel_param].values():
                            result.extend(extract_ids(periodos_data))
                    elif periodo_param in idioma_data[nivel_param]:
                        result.extend(extract_ids(idioma_data[nivel_param][periodo_param]))
    
    return result

result = search(courses, ['iniciante'])
print(result)

result = search(courses, ["ingles"])
print(result)

result = search(courses)
print(result)
