# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import dash_daq as daq
import pandas as pd


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# Load pipeline
pipeline = load('assets/pipeline_drive.joblib')


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Inputs

            Fill out the car specifications

            """
        ),
    # Year    
          html.Div(children='Year', style={
        'textAlign': 'left'}),


        dcc.Input(
                id='input_year',
                placeholder='Enter a year...',
                type='number',
                value='1999',
                className = 'mb-4',
                ),
    # Manufacturer
        html.Div(children='Manufacturer', style={
        'textAlign': 'left'}),

         dcc.Dropdown(
            id='input_manufacturer', 
            options= [
                {'label': 'Acura', 'value': 'acura'},
                {'label': 'Alfa-Romeo', 'value': 'alfa-romeo'},
                {'label': 'Aston-Martin ', 'value': 'aston-martin'},
                {'label': 'Audi', 'value': 'audi'},
                {'label': 'Bmw', 'value': 'bmw'},
                {'label': 'Buick ', 'value': 'buick'},
                {'label': 'Cadillac ', 'value': 'cadillac'},
                {'label': 'Chevrolet ', 'value': 'chevrolet'},
                {'label': 'Chrysler', 'value': 'chrysler'},
                {'label': 'Datsun ', 'value': 'datsun'},
                {'label': 'Dodge ', 'value': 'dodge'},
                {'label': 'Ferrari ', 'value': 'ferrari'},
                {'label': 'Fiat', 'value': 'fiat'},
                {'label': 'Ford ', 'value': 'ford'},
                {'label': 'Gmc ', 'value': 'gmc'},
                {'label': 'Harley-Davidson ', 'value': 'harley-davidson'},
                {'label': 'Hennessey', 'value': 'hennessey'},                
                {'label': 'Honda ', 'value': 'honda'},
                {'label': 'Hyundai ', 'value': 'hyundai'},
                {'label': 'Infiniti ', 'value': 'infiniti'},
                {'label': 'Jaguar ', 'value': 'jaguar'},
                {'label': 'Jeep ', 'value': 'jeep'},
                {'label': 'Kia', 'value': 'kia'},
                {'label': 'Land Rover ', 'value': 'land rover'},
                {'label': 'Lexus ', 'value': 'lexus'},
                {'label': 'Lincoln ', 'value': 'lincoln'},
                {'label': 'Mazda', 'value': 'mazda'},
                {'label': 'Mercedes-Benz', 'value': 'mercedes-benz'},
                {'label': 'Mercury', 'value': 'mercury'},
                {'label': 'Mini ', 'value': 'mini'},
                {'label': 'Mitsubishi', 'value': 'mitsubishi'},
                {'label': 'Morgan ', 'value': 'morgan'},
                {'label': 'Nissan ', 'value': 'nissan'},
                {'label': 'Pontiac ', 'value': 'pontiac'},
                {'label': 'Porsche', 'value': 'porche'},
                {'label': 'Ram ', 'value': 'ram'},
                {'label': 'Rover ', 'value': 'rover'},
                {'label': 'Saturn ', 'value': 'saturn'},
                {'label': 'Subaru', 'value': 'subaru'},
                {'label': 'Tesla ', 'value': 'tesla'},
                {'label': 'Toyota ', 'value': 'toyota'},
                {'label': 'Volkswagen ', 'value': 'volkswagen'},
                {'label': 'Volvo', 'value': 'volvo'},
                {'label': 'Other', 'value': 'nan'}
            ],
            className = 'mb-3',
            value=1
        ),
    # Cylinders    
        html.Div(children='Cylinders', style={
        'textAlign': 'left'}),

        dcc.Slider(
                    id = 'input_cylinders',
                    min=2,
                    max=12,
                    marks={
                            # {'2 cylinders': '2 clndr'},
                            # {'4 cylinders': '4 clndr'},
                            # {'6 cylinders': '6 clndr'},
                            # {'8 cylinders': '8 clndr'},
                            # {'10 cylinders': '10 clndr'},
                            # {'12 cylinders': '12 clndr'}
                                     2: {'label': '2cyln', 'style': {'color': '#77b0b1'}},
                                     4: {'label': '4cyln'},
                                     6: {'label': '6cyln'},
                                     8: {'label': '8cyln'},
                                     10: {'label': '10cyln'},
                                     12: {'label': '12cyln', 'style': {'color': '#f50'}}
                                                            },
                    className = 'mb-3',
                    value=2,
                ),  
    # Fuel
        html.Div(children='Fuel Type', style={
        'textAlign': 'left'}),

        dcc.Dropdown(
            id='input_fuel', 
            options= [
                {'label': 'Gas', 'value': 'gas'},
                {'label': 'Hybrid', 'value': 'hybrid'},
                {'label': 'Electric', 'value': 'electric'},
                {'label': 'Diesel', 'value': 'diesel'},
                {'label': 'Other', 'value': 'nan'}
            ],
            className = 'mb-3',
            value=3
        ),
    # Odometer
        html.Div(children='Odometer', style={
        'textAlign': 'left'
        }),
        dcc.Input(
                id='input_odometer',
                placeholder='Enter a value in miles...',
                type='number',
                className = 'mb-3',
                value='20000'
                ),

    # Drive
         html.Div(children='Drive Type', className = 'mb-1',style={
        'textAlign': 'left'
        }),

        dcc.RadioItems(
                        id='input_drive',
                        options=[
                        {'label': 'Front-Wheel Drive ', 'value': 'fwd'},
                        {'label': 'Rear-Wheel Drive ', 'value': 'rwd'},
                        {'label': 'All-Wheel Drive ', 'value': 'nan'}
                        ],
                        value='fwd',
                        labelStyle={'margin-right': '20px'}
                    )  
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2("Output"),

        # Manufacturer emblem
        html.Div(html.Img(id='manufacturer-image', className= 'img-fluid')),
        
        
        # Miles led display
        html.H3(children='Miles', style={'textAlign': 'left'}, className= 'mt-5'),
        daq.LEDDisplay(
                    id='my-daq-leddisplay',
                    value="10000",
                    className = 'mb-5'
                    ),

    # Prediction output
        html.H2("Prediction"),
        html.Div(id='prediction-content', className='lead'),  

    ]
)

layout = dbc.Row([column1, column2])

# Manufacturer emblem
@app.callback(
                Output('manufacturer-image', 'src'),
                [Input('input_manufacturer', 'value')]
            )

def manufacturer_emblem(input_manufacturer):
    print(f'\n\n{input_manufacturer}\n\n')
    if input_manufacturer == 'acura':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/acura-150x150.png'
        
    elif input_manufacturer == 'aston-martin':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/aston_martin-150x150.png'    
        
    elif input_manufacturer == 'alfa-romeo':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/alfa_romeo-150x150.png'    
        
    elif input_manufacturer == 'audi':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/audi-150x150.png'    
        
    elif input_manufacturer == 'bmw':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/bmw-150x150.png'    
        
    elif input_manufacturer == 'buick':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/buick-150x150.png'    
        
    elif input_manufacturer == 'cadillac':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/cadillac-150x150.png'    
        
    elif input_manufacturer == 'chevrolet':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/chevrolet-150x150.png'    
        
    elif input_manufacturer == 'chrysler':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/chrysler-150x150.png'    
        
    elif input_manufacturer == 'dodge':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/dodge-150x150.png'    
        
    elif input_manufacturer == 'ferrari':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/ferrari-150x150.png'    
        
    elif input_manufacturer == 'fiat':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/fiat-150x150.png'    
        
    elif input_manufacturer == 'ford':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/ford-150x150.png'    
        
    elif input_manufacturer == 'gmc':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/gmc-150x150.png'    
        
    elif input_manufacturer == 'harley-davidson':
        return 'https://simg.nicepng.com/png/small/70-701995_all-harley-davidson-logos-png-harley-davidson-logo.png'    
        
    elif input_manufacturer == 'hennessey':
        return 'https://www.car-logos.org/wp-content/uploads/2011/10/hennessey-150x150.png'    
        
    elif input_manufacturer == 'honda':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/honda-150x150.png'    
        
    elif input_manufacturer == 'hyundai':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/hyundai-150x150.png'    
        
    elif input_manufacturer == 'infiniti':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/inf-150x150.png'    
        
    elif input_manufacturer == 'jaguar':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/jagu-150x150.png'    
        
    elif input_manufacturer == 'jeep':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/jeep-150x150.png'    
        
    elif input_manufacturer == 'kia':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/kia-150x150.png'    
        
    elif input_manufacturer == 'land rover':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/land-rover-150x150.png'    
        
    elif input_manufacturer == 'lexus':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/lexus-150x150.png'    
        
    elif input_manufacturer == 'lincoln':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/linc-150x150.png'    
        
    elif input_manufacturer == 'mazda':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/mazda-150x150.png'    
        
    elif input_manufacturer == 'mercedes-benz':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/marchedrs-150x150.png'    
        
    elif input_manufacturer == 'mercury':
        return 'https://www.martystransmission.com/wp-content/uploads/2018/01/mercury-logo.jpg'    
        
    elif input_manufacturer == 'mini':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/mini-150x150.png'    
        
    elif input_manufacturer == 'mitsubishi':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/mitub-150x150.png'    
        
    elif input_manufacturer == 'morgan':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/morgan-150x150.png'    
        
    elif input_manufacturer == 'nissan':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/nissan-150x150.png'    
        
    elif input_manufacturer == 'pontiac':
        return 'https://p7.hiclipart.com/preview/756/277/149/pontiac-firebird-general-motors-car-pontiac-fiero-explicit-content-logo-thumbnail.jpg'    
        
    elif input_manufacturer == 'porche':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/porsche-150x150.png'    
        
    elif input_manufacturer == 'volvo':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/volvo-150x150.png'    
        
    elif input_manufacturer == 'ram':
        return 'https://lh3.googleusercontent.com/proxy/osC3IbnnPa7376NVw2L3lGSJWhY2mhQbykpT722s15PxMBhwAAE64GJdRDmtJbAWpWgU5s8WZZUhk-qQw-cWeD08ib5TmWt-xFh2e1RB26WPrKk'    
        
    elif input_manufacturer == 'rover':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/land-rover-150x150.png'    
        
    elif input_manufacturer == 'saturn':
        return 'https://i.ya-webdesign.com/images/saturn-car-logo-png-14.png'    
        
    elif input_manufacturer == 'subaru':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/subaru-150x150.png'    
        
    elif input_manufacturer == 'tesla':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/tesla-150x150.png'    
        
    elif input_manufacturer == 'toyota':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/toyota-150x150.png'    
        
    elif input_manufacturer == 'volkswagen':
        return 'https://www.car-logos.org/wp-content/uploads/2011/09/volkswagen-150x150.png'    

    else:
        return 'assets/silhouette-carros-icons-vector.jpg'

# Odometer reading
@app.callback(
    Output(component_id='my-daq-leddisplay', component_property='value'),
    [Input(component_id='input_odometer', component_property='value')]
            )

def update_output_div(input_value):
    return input_value



# Prediction reading
@app.callback(
    Output('prediction-content', 'children'),
    [Input('input_year', 'value'), 
     Input('input_manufacturer', 'value'),
     Input('input_cylinders', 'value'),
     Input('input_fuel', 'value'),
     Input('input_odometer', 'value'),
     Input('input_drive', 'value')],
)
def predict(input_year, input_manufacturer, input_cylinders, input_fuel, input_odometer, input_drive):   
    if input_cylinders == 2:
        input_cylinders = '2 cylinders'
    
    elif input_cylinders == 4:
        input_cylinders = '4 cylinders'
        
    elif input_cylinders == 6:
        input_cylinders = '6 cylinders'
        
    elif input_cylinders == 8:
        input_cylinders = '8 cylinders'
        
    elif input_cylinders == 10:
        input_cylinders = '10 cylinders'
        
    else:
        input_cylinders = '12 cylinders'  
    # Convert input to dataframe
    df = pd.DataFrame(
        data=[[input_year, input_manufacturer, input_cylinders, input_fuel, input_odometer, input_drive]],
        columns=['year', 'manufacturer', 'cylinders', 'fuel', 'odometer', 'drive']
    )

    # Make predictions 
    y_pred = pipeline.predict(df)[0]

    # Show prediction
    return (f'The model predicts this car has a price of ${y_pred:,.0f}')
