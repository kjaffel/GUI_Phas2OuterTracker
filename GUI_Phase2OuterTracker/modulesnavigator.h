#ifndef MODULESNAVIGATOR_H
#define MODULESNAVIGATOR_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class ModulesNavigator; }
QT_END_NAMESPACE

class ModulesNavigator : public QMainWindow
{
    Q_OBJECT

public:
    ModulesNavigator(QWidget *parent = nullptr);
    ~ModulesNavigator();

private:
    Ui::ModulesNavigator *ui;
};
#endif // MODULESNAVIGATOR_H
