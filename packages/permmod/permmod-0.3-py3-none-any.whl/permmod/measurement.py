import os
import pandas as pd
import CoolProp.CoolProp as cp
from .import_data import Data, DataReaktor
from .optimize import Optimizer
from .plots import Plotter, PlotterReaktor


class Measurement:

    def __init__(self, path):
        self.path = path
        self.file_name, _ = os.path.splitext(os.path.split(path)[1])
        self.path_raw, _ = os.path.splitext(os.path.split(path)[0])
        self.path_sim = os.path.join(os.path.dirname(os.path.dirname(path)), 'sim_data')
        self.df_100 = None
        self.df_final = None
        self.sample_data = None

    def guess_permeability(self):
        self.set_data()
        df = self.df_100
        df['V'] = cp.PropsSI('VISCOSITY', 'T', df['Temperature'].to_list(), 'P', df['Outlet_Pressure'].to_list(),
                             self.sample_data['gas'])
        V = self.sample_data['inlet_chamber_volume']
        L = self.sample_data['length']
        A = self.sample_data['area']
        df['k'] = - ((V * df['V'] * 2 * L * df['Inlet_Pressure'].diff()) /
                     (A * (df['Inlet_Pressure'] ** 2 - df['Outlet_Pressure'] ** 2) * df['Duration'].diff()))
        plot = Plotter(df)
        plot.guess_chart()

    def calculate_permeability(self, guess, parameter='k'):
        if self.find_file():
            user_input = input('''
            This measurement has already been evaluated. 
            Do you want to use the time adjusted measurement file? (y/n)''')
            if user_input == 'y':
                self.set_adjusted_data()
            elif user_input == 'n':
                self.set_data()
        else:
            self.set_data()

        result = Optimizer(self.df_100, self.sample_data, guess)
        result, opt_steps = result.nelder_mead(parameter)

        plot = Plotter(self.df_100, **{'name': self.file_name})
        plot.result_chart()

        self.add_results(result, guess)
        user_input = input('Do you want to save the results? (y)')
        if user_input == 'y':
            self.save_adjusted_measurement_file()
            self.save_results()

    def calculate_permeability_stepwise(self, guess, parameter='k'):
        self.set_data()
        data = Data(self.path)
        df_100_list = []
        result_list = []
        temp = pd.DataFrame({'t': [], 'k': []})

        result = Optimizer(self.df_100, self.sample_data, guess)
        result, opt_steps = result.nelder_mead(parameter)
        df_100_list.append(self.df_100)
        result_list.append(result)
        temp.loc[0] = [df_100_list[0]['Duration'].max(), result_list[0].x[0]]

        duration_10_percent = self.df_final['Duration'].max() * 0.1
        for i in range(9):
            self.df_100 = self.df_final[self.df_final['Duration'].between(1, duration_10_percent*(i+1))]
            self.df_100.reset_index(inplace=True, drop=True)
            self.df_100 = data.interpolate(self.df_100)
            result = Optimizer(self.df_100, self.sample_data, guess)
            result, opt_steps = result.nelder_mead(parameter)
            df_100_list.append(self.df_100)
            result_list.append(result)
            temp.loc[i+1] = [df_100_list[-1]['Duration'].max(), result_list[-1].x[0]]

        plot = Plotter(df_100_list, **{'name': self.file_name, 'result': result_list})
        plot.result_chart_stepwise()

        df = df_100_list[0][['Duration', 'DateTime', 'Inlet_Pressure', 'Inlet_Pressure_Cal', 'Outlet_Pressure',
                             'Outlet_Pressure_Cal', 'Confining_Pressure', 'Temperature']]

        path = os.path.join(self.path_sim, self.file_name + '_interval.txt')
        df_res = pd.DataFrame.from_dict(self.sample_data, orient='index')
        df_res.to_csv(path, header=False, sep=':', float_format='%.4f')
        df.to_csv(path, index=False, mode='a', float_format='%.2f')
        temp.to_csv(path, mode='a', index=False)

    def get_solution(self):
        df = pd.read_csv(os.path.join(self.path_sim, self.file_name + '.csv'),
                         nrows=10, sep=':', index_col=0, header=None)
        return [float(df.loc['k', 1]), float(df.loc['n', 1])]

    def set_adjusted_data(self):
        data = Data(self.path)
        self.df_100, self.df_final = data.adjusted_pressure_file()
        self.sample_data = data.sample_data()

    def set_data(self):
        data = Data(self.path)
        self.df_100, self.df_final = data.new_pressure_file()
        self.sample_data = data.sample_data()

    def add_results(self, result, guess):
        try:
            porosity = result.x[1]
        except:
            porosity = guess[1]
        self.sample_data.update({'k': result.x[0],
                                 'n': porosity,
                                 'error': result.fun / 100})

    def save_results(self):
        df = self.df_100[['Duration', 'DateTime', 'Inlet_Pressure', 'Inlet_Pressure_Cal', 'Outlet_Pressure',
                          'Outlet_Pressure_Cal', 'Confining_Pressure', 'Temperature']]

        path = os.path.join(self.path_sim, self.file_name + '.csv')
        df_res = pd.DataFrame.from_dict(self.sample_data, orient='index')
        df_res.to_csv(path, header=False, sep=':', float_format='%.4f')
        df.to_csv(path, index=False, mode='a', float_format='%.2f')
        self.df_final.describe().to_csv(path, mode='a', float_format='%.2f')

    def save_adjusted_measurement_file(self):
        path = os.path.join(self.path_raw, self.file_name + '_adjusted.csv')
        self.df_final.to_csv(path, sep=',', index=False, float_format='%.2f')

    def find_file(self):
        for root, dirs, files in os.walk(self.path_raw):
            if self.file_name + '_adjusted.csv' in files:
                return True
            else:
                return False


class MeasurementReaktor(Measurement):

    def calculate_permeability(self, guess, parameter='k'):
        if self.find_file():
            user_input = input('''
            This measurement has already been evaluated. 
            Do you want to use the time adjusted measurement file? (y/n)''')
            if user_input == 'y':
                self.set_adjusted_data()
            elif user_input == 'n':
                self.set_data()
        else:
            self.set_data()
        result = Optimizer(self.df_100, self.sample_data, guess)
        result, opt_steps = result.nelder_mead(parameter)

        plot = PlotterReaktor(self.df_100, **{'name': self.file_name})
        plot.result_chart()

        self.add_results(result, guess)
        user_input = input('Do you want to save the results? (y)')
        if user_input == 'y':
            self.save_adjusted_measurement_file()
            self.save_results()

    def set_data(self):
        data = DataReaktor(self.path)
        self.df_100, self.df_final = data.new_pressure_file()
        self.sample_data = data.sample_data()

    def set_adjusted_data(self):
        data = DataReaktor(self.path)
        self.df_100, self.df_final = data.adjusted_pressure_file()
        self.sample_data = data.sample_data()

    def save_results(self):
        df = self.df_100[['Duration', 'DateTime', 'Inlet_Pressure', 'Inlet_Pressure_Cal', 'Outlet_Pressure',
                          'Outlet_Pressure_Cal', 'Confining_Pressure_Reactor', 'Confining_Pressure_Sample',
                          'Temperature']]

        path = os.path.join(self.path_sim, self.file_name + '.csv')
        df_res = pd.DataFrame.from_dict(self.sample_data, orient='index')
        df_res.to_csv(path, header=False, sep=':', float_format='%.4f')
        df.to_csv(path, index=False, mode='a', float_format='%.2f')
        self.df_final.describe().to_csv(path, mode='a', float_format='%.2f')
