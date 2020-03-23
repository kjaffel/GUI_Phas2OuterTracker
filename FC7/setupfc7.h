#ifndef SETUPFC7_H
#define SETUPFC7_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class setupFC7; }
QT_END_NAMESPACE

class setupFC7 : public QMainWindow
{
    Q_OBJECT

public:
    setupFC7(QWidget *parent = nullptr);
    ~setupFC7();

private:
    Ui::setupFC7 *ui;
};
#endif // SETUPFC7_H
