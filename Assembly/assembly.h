#ifndef ASSEMBLY_H
#define ASSEMBLY_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class Assembly; }
QT_END_NAMESPACE

class Assembly : public QMainWindow
{
    Q_OBJECT

public:
    Assembly(QWidget *parent = nullptr);
    ~Assembly();

private:
    Ui::Assembly *ui;
};
#endif // ASSEMBLY_H
