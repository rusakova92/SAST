import git
import subprocess
from docx import Document

# Клонируем репозиторий
repo_url = 'https://github.com/rusakova92.git'
repo_dir = 'repository_folder'
repo = git.Repo.clone_from(repo_url, repo_dir)

# Запуск SAST-анализатора
output = subprocess.check_output(['SAST_analyzer', repo_dir])

# Создание документ с результатами анализа
doc = Document()
doc.add_heading('Результаты анализа уязвимостей', level=1)
doc.add_paragraph('Репозиторий: {}'.format(repo_url))
doc.add_paragraph('Результаты анализа:')
doc.add_paragraph(output.decode('utf-8'))

doc.save('report.docx')
