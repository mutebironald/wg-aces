npm install
invoke bootstrap-wger --settings-path ./settings.py --no-start-server
python manage.py makemigrations --merge
python manage.py migrate
echo "Done running release scripts"
