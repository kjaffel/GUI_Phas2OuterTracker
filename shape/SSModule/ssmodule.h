#ifndef SSMODULE_H
#define SSMODULE_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class SSModule; }
QT_END_NAMESPACE

class SSModule : public QMainWindow
{
    Q_OBJECT

public:
    SSModule(QWidget *parent = nullptr);
    ~SSModule();

private:
    Ui::SSModule *ui;
};
#endif // SSMODULE_H
