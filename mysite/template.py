from django.template import Template, Context
import datetime

raw_template = """<p> Querido {{person_name}}, </p>
				<p> Gracias por tu encargo desde {{company}}.
				Su encargo sera enviado en {{ship_date|date:"F j, Y"}} </p>

				{% if ordered_warranty %}
				<p>  Tu garantia estara incluida en el paquete. </p>
				{% else %}
				<p> No ordenaste garantia, asi que suerte XD </p>
				{% endif %}

				<p> Sinceramente, {{company}} </p>"""

t = Template(raw_template)
c = Context({'person_name' : 'Raul',
			'company' : 'TIMSA',
			'ship_date' : datetime.date(2009,4,2),
			'ordered_warranty' : False})

t.render(c)

