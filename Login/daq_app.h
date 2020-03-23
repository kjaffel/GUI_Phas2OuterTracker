#ifndef DAQ_APP_H
#define DAQ_APP_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class DAQ_APP; }
QT_END_NAMESPACE

class DAQ_APP : public QMainWindow
{
    Q_OBJECT

public:
    DAQ_APP(QWidget *parent = nullptr);
    ~DAQ_APP();

private:
    Ui::DAQ_APP *ui;

private slots:
	void on_findButton_clicked();

private:
	Ui::DAQ_APP *ui;
	void loadTextFile();
};
#endif // DAQ_APP_H
