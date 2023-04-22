import os
import shutil
import subprocess
import re
from random import sample, randint
from PyPDF2 import PdfMerger

tema = 'Recuperação de Matemática - Bimestre I'
qtd = 160

latex_main = 'main.tex'

parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
provas_dir = os.path.join(parent_dir, 'provas')
pdfs_dir = os.path.join(parent_dir, 'pdfs')
pdfs_resp_dir = os.path.join(parent_dir, 'pdfs_resp')
regex_tema = '@tema@'

def questao1(data):
    conj_A = set(sample(range(-5, 5), 4))
    conj_B = set(sample(range(-5, 5), 5))
    conj_C = set(sample(range(-5, 5), 6))
    conj_AuB = conj_A | conj_B
    conj_AiB = conj_A & conj_B
    conj_AdC = conj_A - conj_C
    conj_AuBdC = conj_AuB - conj_C
    conj_BuCdAiB = (conj_B | conj_C) - conj_AiB
    data = re.sub("@q1conj_A@", str(conj_A)[:-1], data)
    data = re.sub("@q1conj_B@", str(conj_B)[:-1], data)
    data = re.sub("@q1conj_C@", str(conj_C)[:-1], data)
    data = re.sub("@q1sA@", str(conj_AuB), data)
    data = re.sub("@q1sB@", str(conj_AiB), data)
    data = re.sub("@q1sC@", str(conj_AdC), data)
    data = re.sub("@q1sD@", str(conj_AuBdC), data)
    data = re.sub("@q1sE@", str(conj_BuCdAiB), data)

    return data

def questao2(data):
    conj_A = set(sample(range(-7, 10), 8))
    conj_B = set(sample(range(-7, 10), 8))
    conj_AdB = conj_A - conj_B
    conj_BdA = conj_B - conj_A
    conj_AuB = conj_A | conj_B
    conj_AiB = conj_A & conj_B
    data = re.sub("@q2conj_AdB@", str(conj_AdB)[:-1], data)
    data = re.sub("@q2conj_BdA@", str(conj_BdA)[:-1], data)
    data = re.sub("@q2conj_AuB@", str(conj_AuB)[:-1], data)
    data = re.sub("@q2sAdB@", str(conj_AdB), data)
    data = re.sub("@q2sBdA@", str(conj_BdA), data)
    data = re.sub("@q2sAiB@", str(conj_AiB), data)

    return data

def questao3(data):
    a = sample(range(-10, 10), 2)
    a.sort()
    a2 = [
        ']' if randint(0, 100) < 50 else '[',
        '[' if randint(0, 100) < 50 else ']'
        ]
    a_colc = f"{a2[0]} {a[0]},{a[1]}{a2[1]}"
    data = re.sub("@q3A@", a_colc[:-1], data)
    data = re.sub("@q3A2@", a_colc[-1:], data)
    a = sample(range(-10, 10), 2)
    a.sort()
    a2 = [
        '<' if randint(0, 100) < 50 else r'\\leq',
        '<' if randint(0, 100) < 50 else r'\\leq'
        ]
    a_chav = f"{a[0]} {a2[0]} x {a2[1]} {a[1]}"
    data = re.sub("@q3B@", a_chav, data)
    a = randint(-10, 10)
    a2 = ']t' if randint(0, 100) < 50 else '[]'
    a_colc = f"{a}{a2[:-1]}"
    data = re.sub("@q3C@", a_colc[:-1], data)
    data = re.sub("@q3C2@", a_colc[-1:], data)
    a = sample(range(-10, 10), 2)
    a.sort()
    a2 = [
        '<' if randint(0, 100) < 50 else r'\\leq',
        '<' if randint(0, 100) < 50 else r'\\leq'
        ]
    a_chav = f"{a[0]} {a2[0]} x {a2[1]} {a[1]}"
    data = re.sub("@q3D@", a_chav, data)

    return data

def questao4(data):
    mhs = randint(10, 50)
    sh = randint(mhs, mhs + 150)
    ms = randint(mhs, mhs + 150)
    mh = randint(mhs, mhs + 150)
    s = randint(mhs + sh + ms, mhs + sh + ms + 200)
    h = randint(mhs + sh + mh, mhs + sh + mh + 200)
    m = randint(mhs + ms + mh, mhs + ms + mh + 200)
    t = randint(
            s + h + m - sh - ms - mh + mhs,
            s + h + m - sh - ms - mh + mhs + 350
            )
    u = s + h + m - sh - ms - mh + mhs

    n_sh = sh - mhs
    n_ms = ms - mhs
    n_mh = mh - mhs
    n_s = s - (n_sh + n_ms + mhs)
    n_h = h - (n_sh + n_mh + mhs)
    n_m = m - (n_mh + n_ms + mhs)

    a = n_s + n_h + n_m
    b = t - u
    c = n_sh + n_ms + n_mh + mhs

    data = re.sub("@q4mhs@", str(mhs), data)
    data = re.sub("@q4sh@", str(sh), data)
    data = re.sub("@q4ms@", str(ms), data)
    data = re.sub("@q4mh@", str(mh), data)
    data = re.sub("@q4s@", str(s), data)
    data = re.sub("@q4h@", str(h), data)
    data = re.sub("@q4m@", str(m), data)
    data = re.sub("@q4t@", str(t), data)

    data = re.sub("@q4smhs@", str(mhs), data)
    data = re.sub("@q4ssh@", str(n_sh), data)
    data = re.sub("@q4sms@", str(n_ms), data)
    data = re.sub("@q4smh@", str(n_mh), data)
    data = re.sub("@q4ss@", str(n_s), data)
    data = re.sub("@q4sH@", str(n_h), data)
    data = re.sub("@q4sm@", str(n_m), data)
    data = re.sub("@q4sa@", str(a), data)
    data = re.sub("@q4sb@", str(b), data)
    data = re.sub("@q4sc@", str(c), data)

    return data

def questao5(data):
    nAuB = randint(10, 30)
    AiB = randint(20, 40)
    x = 100 - (nAuB + AiB)
    AdB = randint(0, x - 5)
    BdA = x - AdB
    nAiB = AiB * 2
    # t = 100 * nAiB/AiB

    data = re.sub("@q5AdB@", str(AdB), data)
    data = re.sub("@q5BdA@", str(BdA), data)
    data = re.sub("@q5nAuB@", str(nAuB), data)
    data = re.sub("@q5nAiB@", str(nAiB), data)

    data = re.sub("@q5sAiB@", str(AiB), data)
    data = re.sub("@q5sAdB@", str(AdB), data)
    data = re.sub("@q5sBdA@", str(BdA), data)

    return data

# creating provas directory
if not os.path.isdir(provas_dir):
    os.mkdir(provas_dir)
if not os.path.isdir(pdfs_dir):
    os.mkdir(pdfs_dir)
if not os.path.isdir(pdfs_resp_dir):
    os.mkdir(pdfs_resp_dir)

# copying files from parent folder to provas dir
shutil.copytree(
        os.path.join(parent_dir, 'figures'),
        os.path.join(provas_dir, 'figures'),
        dirs_exist_ok=True
        )

for i in range(qtd):
    # copying tex file to folder
    shutil.copy2(
            os.path.join(parent_dir, latex_main),
            os.path.join(provas_dir)
            )

    with open(os.path.join(provas_dir, latex_main),
              'r', encoding='utf-8') as file:
        main_tex = file.read()

    # disabling printanswers
    # replacing tema_token
    main_tex = re.sub(regex_tema, f"{tema} - Prova Tipo {i + 1}", main_tex)
    main_tex = questao1(main_tex)
    main_tex = questao2(main_tex)
    main_tex = questao3(main_tex)
    main_tex = questao4(main_tex)
    main_tex = questao5(main_tex)

    for j in range(2):
        if j == 0:
            pass
        else:
            main_tex = re.sub(r'%\\printanswers', r'\\printanswers', main_tex)
        # saving main_tex file
        with open(
                os.path.join(provas_dir, latex_main),
                'w', encoding='utf-8') as file:
            file.write(main_tex)

        # call pdf latex cleaning files
        subprocess.call([
            'latexmk',
            '-C',
            os.path.join(provas_dir, latex_main),
            '-quiet'
            ])

        # call pdf latex generating pdf
        subprocess.call([
            'latexmk',
            '-pdf',
            os.path.join(provas_dir, latex_main),
            f"--output-directory={os.path.join(provas_dir)}",
            '-quiet'
            ])
        if j == 0:
            shutil.move(
                    os.path.join(provas_dir, 'main.pdf'),
                    os.path.join(pdfs_dir, f"main_{i}.pdf")
                    )
        else:
            shutil.move(
                    os.path.join(provas_dir, 'main.pdf'),
                    os.path.join(pdfs_resp_dir, f"main_{i}.pdf")
                    )


# merging pdfs
merger = PdfMerger()
merger2 = PdfMerger()

for i in range(qtd):
    merger.append(os.path.join(pdfs_dir, f"main_{i}.pdf"))
    merger2.append(os.path.join(pdfs_resp_dir, f"main_{i}.pdf"))

merger.write(os.path.join(parent_dir, f"{tema}.pdf"))
merger2.write(os.path.join(parent_dir, f"{tema} - Respostas.pdf"))
merger.close()
merger2.close()

shutil.rmtree(provas_dir)
shutil.rmtree(pdfs_dir)
shutil.rmtree(pdfs_resp_dir)
