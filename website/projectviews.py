from flask import Blueprint, render_template, redirect, url_for, request, flash

project_views = Blueprint('project_views', __name__, static_folder = 'static', template_folder = 'projects')



@project_views.route('drawmach')
@project_views.route('drawingmachine')
def drawmach():
    return render_template('drawmach.html')

@project_views.route('arm')
@project_views.route('robotarm')
def robotarm():
    return render_template('robotarm.html')


@project_views.route('gyro')
@project_views.route('gyroscope')
def gyroscope():
    return render_template('gyroscope.html')


@project_views.route('solidworksfluid')
@project_views.route('fluidsim')
def solidworksfluid():
    return render_template('solidworksfluid.html')


@project_views.route('topologystudy')
@project_views.route('topologysim')
def topologystudy():
    return render_template('topologystudy.html')


@project_views.route('sdp')
@project_views.route('truss')
def trussSDP():
    return render_template('trussSDP.html')


