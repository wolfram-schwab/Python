from pathlib import Path

def base_dir() :
    base = Path.cwd()
    if not str(base).endswith('mysite') :
        base = base.joinpath('mysite')
    return base

def __traverse(file, files) :
    files.append(file)
    if file.is_dir() :
        for f in file.iterdir() :
            if '__' not in str(f) : 
                __traverse(f, files)

def filesystem() :
    files = []
    file = Path.cwd()
    __traverse(file, files)
    html = ""
    current_dir = files[0]
    tiefe = 0
    for file in files :
        if len(file.parts) != tiefe :
            html += "\n</li></ul><ul><li class='dir'>"
            tiefe = len(file.parts)
        if file.is_dir() :
            html += ""
            if len(file.parts) > tiefe :
                tiefe += 1
        else : html += '<li>'
        html += str(file.parts[-1])
        if not file.is_dir() : html += "</li>"
        if (file.is_dir()
            and len(file.parts) < tiefe) :
            tiefe = len(file.parts)
    return html

if __name__ == '__main__' :
    files = filesystem()
    print(files)
    
    