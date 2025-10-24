#include "autocalibrate_seconds.h"

namespace esphome {
namespace ld2410 {

void AutocalibrateSeconds::control(float value) {
  if (value < 1.0f)
    value = 1.0f;
  if (value > 600.0f)
    value = 600.0f;
  this->parent_->set_autocal_seconds(static_cast<uint16_t>(value));
  this->publish_state(value);
}

}  // namespace ld2410
}  // namespace esphome
