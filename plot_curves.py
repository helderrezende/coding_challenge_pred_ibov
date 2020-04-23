from matplotlib import pyplot

def plot_learning_curve(model, error_type='rmse'):
    results = model.evals_result()
    epochs = len(results['validation_0'][error_type])
    x_axis = range(0, epochs)

    fig, ax = pyplot.subplots()
    ax.plot(x_axis, results['validation_0'][error_type], label='Train')
    ax.plot(x_axis, results['validation_1'][error_type], label='Test')
    ax.legend()
    pyplot.ylabel('Log Loss')
    pyplot.title('XGBoost Log Loss')
    pyplot.show()