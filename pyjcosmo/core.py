import math
from py4j.java_gateway import JavaGateway, GatewayParameters

class JCosmoWrapper:
    def __init__(self, port=25333):
        try:
            # We set a short timeout so the user doesn't wait forever
            params = GatewayParameters(port=port, read_timeout=2)
            self.gateway = JavaGateway(gateway_parameters=params, auto_field=True)
            self.JCOSMO = self.gateway.entry_point
            
            # Heartbeat check: attempt to access a simple field
            # This triggers the Py4JNetworkError immediately if JCOSMO is off
            _ = self.JCOSMO.getClass().getName()
            
        except Exception:
            raise ConnectionError(
                f"\n\n[JCOSMO Error] Could not connect to the Java gateway on port {port}.\n"
                "Make sure JCOSMO is running and the Py4J Gateway is enabled."
            ) from None
        
    def list_models(self):
        """Returns a list of available models."""
        return self.JCOSMO.listModels()

    def get_model(self, model_name='CS25'):
        """Returns a configured model instance."""
        return CosmoModel(self.JCOSMO.newModel(model_name), self.gateway)

class CosmoModel:
    def __init__(self, model_instance, gateway):
        self.model = model_instance
        self.gateway = gateway
        self._ncomps = 0

    def find_compounds(self, search_query):
        """
        Searches the JCOSMO database for compounds matching the query.
        Example: model.find_compounds('+1') for cations.
        """
        # Returns a Java List, but Python can iterate over it directly
        results = self.model.findCompound(search_query)
        return list(results)

    def set_compounds(self, compounds):
        """Pass a Python list of strings."""
        self._ncomps = len(compounds)
        java_array = self.gateway.new_array(self.gateway.jvm.java.lang.String, self._ncomps)
        for i, name in enumerate(compounds):
            java_array[i] = name
        self.model.setCompounds(java_array)
    
    def set_ignore_fh(self, ignore):
        """Optionally ignore the FH combinatorial term."""
        self.model.setIgnoreFH(ignore)

    def set_use_voutsas_fv(self, ignore):
        """Use Voutsas et al (1995) exponent in the FH combinatorial term."""
        self.model.setUseFV(ignore)

    def set_temperature(self, t_kelvin):
        self.model.setTemperature(float(t_kelvin))

    def set_composition(self, x_list):
        """Pass a Python list of floats."""
        if len(x_list) != self._ncomps:
            raise ValueError(f"Expected {self._ncomps} fractions, got {len(x_list)}")
        java_x = self.gateway.new_array(self.gateway.jvm.double, self._ncomps)
        for i, val in enumerate(x_list):
            java_x[i] = float(val)
        self.model.setComposition(java_x)

    def get_gamma_ln(self):
        """Returns activity coefficients as a Python list."""
        res = self.model.activityCoefficientLn()
        return [res[i] for i in range(self._ncomps)]

    def get_excess_enthalpy(self):
        """Returns hE/RT."""
        return self.model.excessEnthalpy()
    
    def get_excess_gibbs(self):
        """Returns gE/RT."""
        return self.model.excessGibbs()
    