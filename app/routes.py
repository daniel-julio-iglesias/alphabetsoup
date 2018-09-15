#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Views
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, DocForm
from app.mainapp import MainApp
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
import os
from config import basedir


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Daniel'}
    return render_template('index.html', title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/sectionsextract', methods=['GET', 'POST'])
@login_required
def sectionsextract():
    """ Adapt to your functionality
    """
    form = DocForm()
    if form.validate_on_submit():

        # training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train')
        training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train', '00010Preface')
        # doc = form.document.data
        doc = '01.txt'
        training_dir = training_dir + os.sep
        mba = MainApp(training_dir, doc)
        content = mba.extract()

        flash('Document Section Extracted for  document {}, content {}'.format(
             form.doc.data, content))
        # return redirect(url_for('index'))

        return render_template('alphabetsoup.html', title='Document Sections Extractor', form=form)
    return render_template('alphabetsoup.html', title='Document Sections Extractor', form=form)
