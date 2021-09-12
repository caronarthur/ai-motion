web: sh setup.sh && streamlit run app.py
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt
heroku buildpacks
# Should show apt first, then python