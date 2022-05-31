from router import *
from controllers.population import *

Route.get('/v1/charts/population', PopulationController.largest, {
    'type': 'largest'
})

Route.get('/v1/charts/population', PopulationController.process, {
    'type': 'process'
})
